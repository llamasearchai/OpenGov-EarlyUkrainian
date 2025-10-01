import json
import typer
from rich.console import Console
from rich.table import Table
from opengov_earlyukrainian.core.alphabet import AlphabetTeacher
from opengov_earlyukrainian.core.cases import CasesTeacher
from opengov_earlyukrainian.core.verbs import VerbConjugator
from opengov_earlyukrainian.core.transliteration import Transliterator
from opengov_earlyukrainian.core.business import BusinessUkrainian
from opengov_earlyukrainian.core.culture import CulturalGuide

app = typer.Typer(
    help="OpenGov-EarlyUkrainian CLI - Ukrainian Language Learning Platform"
)
console = Console()


@app.command()
def alphabet(row: str = typer.Argument("iotated", help="Row name: iotated, basic, vowels")):
    """Display Ukrainian alphabet row with letters."""
    t = AlphabetTeacher()
    result = t.get_row(row)
    console.print(f"\n[bold cyan]Alphabet Row:[/bold cyan] {result['row']}")
    console.print(f"[yellow]Letters:[/yellow] {', '.join(result['letters'])}\n")


@app.command()
def decline(
    noun: str = typer.Argument(..., help="Noun to decline"),
    gender: str = typer.Argument(..., help="Gender: feminine, masculine, neuter"),
):
    """Decline a Ukrainian noun through all cases."""
    c = CasesTeacher()
    result = c.decline_noun(noun, gender)

    table = Table(title=f"Declension of '{noun}' ({gender})")
    table.add_column("Case", style="cyan", no_wrap=True)
    table.add_column("Form", style="yellow")

    for case, form in result.items():
        table.add_row(case, form)

    console.print()
    console.print(table)
    console.print()


@app.command()
def conjugate(
    verb: str = typer.Argument(..., help="Verb to conjugate"),
    tense: str = typer.Option("present", help="Tense: present, past"),
):
    """Conjugate a Ukrainian verb."""
    v = VerbConjugator()
    result = v.conjugate(verb, tense)

    if not result.get("forms"):
        console.print(f"[red]Could not conjugate '{verb}' in {tense} tense[/red]")
        return

    table = Table(title=f"Conjugation of '{verb}' ({tense})")
    table.add_column("Person", style="cyan", no_wrap=True)
    table.add_column("Form", style="yellow")

    for person, form in result["forms"].items():
        table.add_row(person, form)

    console.print()
    console.print(table)
    console.print()


@app.command()
def translit(text: str = typer.Argument(..., help="Latin text to transliterate")):
    """Transliterate Latin text to Ukrainian."""
    tr = Transliterator()
    result = tr.to_ukrainian(text)
    console.print(f"\n[bold cyan]Latin:[/bold cyan] {text}")
    console.print(f"[bold yellow]Ukrainian:[/bold yellow] {result}\n")


@app.command()
def aspect(verb: str = typer.Argument(..., help="Imperfective verb")):
    """Get aspect pair for a verb."""
    v = VerbConjugator()
    perfective = v.aspect_pair(verb)
    console.print(f"\n[cyan]Imperfective:[/cyan] {verb}")
    console.print(f"[yellow]Perfective:[/yellow] {perfective}\n")


@app.command()
def business(
    purpose: str = typer.Option("meeting", help="Template type: meeting, follow_up")
):
    """Get business Ukrainian email templates."""
    b = BusinessUkrainian()
    template = b.email_template(purpose)

    console.print(f"\n[bold cyan]Business Template:[/bold cyan] {purpose}")
    console.print(f"\n[yellow]Subject:[/yellow] {template['subject']}")
    console.print(f"\n[yellow]Body:[/yellow]\n{template['body']}")
    console.print(f"\n[yellow]Signoff:[/yellow]\n{template['signoff']}\n")


@app.command()
def culture():
    """Display Ukrainian cultural information."""
    guide = CulturalGuide()

    console.print("\n[bold cyan]Ukrainian Regions:[/bold cyan]")
    for region in guide.regions():
        console.print(f"  - {region}")

    console.print("\n[bold cyan]Holidays:[/bold cyan]")
    for holiday, desc in guide.holidays().items():
        console.print(f"  [yellow]{holiday}:[/yellow] {desc}")

    console.print("\n[bold cyan]Business Etiquette:[/bold cyan]")
    for rule in guide.etiquette():
        console.print(f"  - {rule}")
    console.print()


@app.command()
def version():
    """Show version information."""
    from opengov_earlyukrainian import __version__

    console.print(f"\n[bold cyan]OpenGov-EarlyUkrainian[/bold cyan] v{__version__}")
    console.print("[yellow]Author:[/yellow] Nik Jois <nikjois@llamasearch.ai>\n")


if __name__ == "__main__":
    app()

