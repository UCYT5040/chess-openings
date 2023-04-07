# Chess Openings

A program to fetch chess openings from the [chess.com](https://www.chess.com/openings) website.

## Usage

### Install dependencies

```bash
$ pip3 install -r requirements.txt
```

### Run the program

Download all the openings to a file called `openings.json`:

```bash
$ python3 main.py
```

Download the openings by page on the website:

```bash
$ python3 main.py --seperate_pages=True
```

## License

```text
Copyright [2023] [UCYT5040 / Jeremiah Saunders]

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
```
