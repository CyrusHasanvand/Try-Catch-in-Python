# Writing Candle Data to Text File with Try-Except in Python

This repository demonstrates how to safely write candlestick price data (High, Low, Open, Close) to a text file using Python's `try-except-finally` structure.

## Description

The script defines sample price data and writes it to a file called `Candle Information.txt`. It uses a `while` loop with a `try-except` block to ensure that the file is written successfully, even if an unexpected error occurs during the file-writing process.

The `finally` block prints a message each time the process is attempted.

## How to Run

```bash
python write_candle_info.py
```
## Example Output (`Candle Information.txt`)

