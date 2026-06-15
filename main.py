#!/usr/bin/env python3
"""
Simple Python Torrent-like App
Educational demo for downloading torrents and basic P2P.
"""

import argparse
import sys
import time
from rich.console import Console
from rich.progress import Progress, SpinnerColumn, TextColumn, BarColumn, DownloadColumn, TimeRemainingColumn
import os

console = Console()

def simulate_download(magnet_or_url: str, save_path: str = "."):
    """Simple simulation for demo purposes"""
    console.print(f"[bold green]Starting download for:[/bold green] {magnet_or_url}")
    console.print(f"Saving to: {save_path}")

    # Simulate progress
    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        BarColumn(),
        DownloadColumn(),
        TimeRemainingColumn(),
        console=console,
    ) as progress:
        task = progress.add_task("[cyan]Downloading...", total=100)
        for i in range(100):
            progress.update(task, advance=1)
            time.sleep(0.05)
    console.print("[bold green]✅ Download completed![/bold green]")
    console.print(f"File saved as: example_file.iso in {save_path}")

def main():
    parser = argparse.ArgumentParser(description="Python Torrent-like App")
    parser.add_argument("magnet", nargs="?", help="Magnet link or torrent URL")
    parser.add_argument("-o", "--output", default=".", help="Output directory")
    parser.add_argument("--share", action="store_true", help="Start simple file sharing mode")

    args = parser.parse_args()

    if args.share:
        console.print("[yellow]File sharing mode started (demo).[/yellow]")
        console.print("In a real app this would seed files to peers.")
        # Simple server simulation
        from http.server import HTTPServer, SimpleHTTPRequestHandler
        os.chdir(args.output)
        server = HTTPServer(("0.0.0.0", 8080), SimpleHTTPRequestHandler)
        console.print("[green]Serving at http://0.0.0.0:8080[/green]")
        server.serve_forever()
        return

    if not args.magnet:
        console.print("[red]Error:[/red] Please provide a magnet link or torrent URL.")
        parser.print_help()
        sys.exit(1)

    simulate_download(args.magnet, args.output)

if __name__ == "__main__":
    main()