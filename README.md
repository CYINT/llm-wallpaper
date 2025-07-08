# llm-wallpaper

`llm-wallpaper` is an experimental cross-platform Python application that uses an LLM to help generate wallpapers. It works on macOS and Windows and can be extended to pull various inputs such as screenshots or recent X posts to influence the wallpaper prompt.

## Features

- Generate wallpapers using your favorite LLM provider.
- Works on macOS and Windows.
- Change wallpapers on a schedule or on demand.
- Customize the prompt sent to the LLM.
- Optional inputs such as screenshots or X posts can be added.

## Installation

```bash
# Clone the repository and install dependencies
pip install -r requirements.txt
```

You will need an API key for a provider that supports image generation (for example, OpenAI). Set the key using an environment variable or pass `--llm-key` on the command line.

## Usage

```bash
python wallpaper.py --prompt "sunset over mountains" --interval 60 --inputs screenshot
```

Arguments:

- `--llm-key` – API key for the LLM. Can also be provided via `OPENAI_API_KEY`.
- `--prompt` – Base prompt for the LLM.
- `--interval` – Interval (minutes) for changing the wallpaper. If omitted, a single wallpaper is generated.
- `--inputs` – Comma-separated list of inputs (e.g. `screenshot,xposts`).

## Contributing

Contributions are welcome! Fork the repo and submit a pull request. Please follow standard Python formatting via `black` and keep changes focused. For major features, open an issue first to discuss your ideas.

1. Fork the repository and create your branch.
2. Commit your changes with clear messages.
3. Open a pull request describing your changes.

## Donations

If you find this project useful, consider donating to help sustain development.

- BTC: `bc1qq7tsvfkfcyaqy8jxz9n3v93h0uw6frw0p4jau5`

## License

This project is released under the MIT License. See [LICENSE](LICENSE) for details.
