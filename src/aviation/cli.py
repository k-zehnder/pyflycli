"""This module provides the Pyfly CLI."""
import time
from typing import List, Optional
import typer

from aviation.errors import *
from aviation.config import init_app, _init_database
from aviation.database import AsyncDatabaseHandler, DummyAsyncDatabaseHandler
from aviation.utils import Console, TablePrinter


tp = TablePrinter()
app = typer.Typer()

        
@app.command()
def init():
    """Initialize the Pyfly app."""
    log = Log()
    app_init_error = init_app()
    if app_init_error:
        log.app_error()
        raise typer.Exit(1)
    log.healthy()
    
@app.command(name="responses")
def list_all_responses() -> None:
    """List all Responses."""
    handler =  AsyncDatabaseHandler()
    all_responses = handler.run("get_all_responses")
    if len(all_responses) == 0:
        typer.secho(
            "There are no Response in the DB yet", fg=typer.colors.RED
        )
        raise typer.Exit()
    tp.print_response(all_responses)
  
@app.command(name="detailed")
def list_all_detailed() -> None:
    """List all DetailedFlights."""
    handler =  AsyncDatabaseHandler()
    all_flights = handler.run("get_all_detailed")
    if len(all_flights) == 0:
        typer.secho(
            "There are no Flights in the DB yet", fg=typer.colors.RED
        )
        raise typer.Exit()    
    tp.print_detailed(all_flights)

@app.command(name="brief")
def list_all_brief() -> None:
    """List all BriefFlights."""
    handler =  AsyncDatabaseHandler()
    all_flights = handler.run("get_all_brief")
    if len(all_flights) == 0:
        typer.secho(
            "There are no Flights in the DB yet", fg=typer.colors.RED
        )
        raise typer.Exit()    
    tp.print_brief(all_flights)



