# CashMemo

A desktop GUI application built using Python and Tkinter for generating, viewing, and exporting itemized bills and receipts.

## Features

* **Item Management:** Enter item names, quantity, and unit price with automatic total calculation ($Total = \text{Price} \times \text{Quantity}$).
* **Input Validation:** Built-in validation to ensure item names do not exceed 18 characters and numerical values are properly formatted.
* **Interactive Display:** Scrollable listbox view displaying itemized receipt entries in real-time.
* **Export Functionality:** Export created cash memos directly to standard text (`.txt`) files.
* **Clear & Reset:** Fast memory cleanup with a single click to start a new receipt.

## Prerequisites

Ensure you have Python installed on your system:

* **Python:** `3.x`
* **Tkinter:** Included with standard Python installations on Windows and macOS. Linux users may need to install `python3-tk`.

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/musaddiq-sultan/CashMemo.git
   cd CashMemo
   ```

2. Run the application directly (no external pip dependencies required).

## How to Use

To start the graphical interface, execute the main script:

```
python main.py
```

### Steps to Generate and Export a Memo

1. **Add Items:**
   * Type the **Item Name** (max 18 characters).
   * Enter the **Quantity** (numeric value).
   * Enter the **Unit Price** (numeric value).
   * Click **Submit**. The entry and its calculated total will be listed in the Data frame.

2. **Clear Data:**
   * Click **Clear** to wipe all current items displayed in the memo view.

3. **Export Receipt:**
   * Click **Export** to open the file save dialog.
   * Choose a location and file name to save your generated memo as a text file.