# Candle price information
High = 6010
Low = 6003
Open = 6004
Close = 6008

# Below, it is an attempt to write the information into a file using try-except
while True:
    try:
        with open("Candle Information.txt", "w") as f:
            f.write(
                "\nCandle Info:\n"
                "High Price: %.2f\n"
                "Low Price: %.2f\n"
                "Open Price: %.2f\n"
                "Close Price: %.2f\n" % (High, Low, Open, Close)
            )
        print("File written successfully.")
        break  # Exit loop if successful
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        print("The process will check again.\n")
