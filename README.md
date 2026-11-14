# PhoNumSpy

PhoNumSpy is an OSINT tool that collects basic information about a phone number, such as location, country code, and carrier. It also runs a web footprint search and a targeted search across temporary phone number providers.

> **Legal notice:** Use this tool only on phone numbers you are authorized to research, and only for lawful purposes. You are responsible for complying with applicable laws and the terms of service of any site you query.

## Features

- Phone number information: time zone(s), country code, and carrier
- Web footprint search for the phone number
- Targeted search across online temporary phone number providers
- Results saved to a TXT file

## Requirements

- Python 3.8 or newer
- `pip` and `venv`
- An internet connection
- A `websites.txt` file in the working directory, containing one provider domain per line (used by the targeted search)

## Installation

```bash
# clone the repository
git clone https://github.com/0xDurmus/PhoNumSpy.git

# enter the project directory
cd PhoNumSpy

# create and activate a virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate

# install dependencies
pip install -r requirements.txt
```

### Kali Linux / Debian

Kali blocks system-wide `pip install` (PEP 668), so use a virtual environment as shown above. If the venv module is missing, run:

```bash
sudo apt update && sudo apt install -y python3-venv python3-pip
```

## Usage

```bash
python3 PhoNumSpy.py
```

Enter the number in international format, starting with `+` and the country code:

```
Input the target phone number using this format: +(prefix)(phonenumber) ES: +447455869664
-->
```

When the scan finishes, the results are saved in the current directory as `<number>_results.txt`.

## Known Issues

- `PhoNumSpy.py` contains `import googlesearch-python`, which is not valid Python syntax, so the script fails to start. The import should be `from googlesearch import search` only.
- `requirements.txt` lists `time`, which is part of the Python standard library and cannot be installed with pip. Remove that line before running `pip install -r requirements.txt`.
- `requirements.txt` lists both `googlesearch` and `googlesearch-python`. Keep only one of them.
- The script reads `websites.txt`, but this file is not included in the repository.

## License

This project is licensed under the terms in the [LICENSE](LICENSE) file.
