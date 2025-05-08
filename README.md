# 🌀 Fibonacci Generator

This Python script generates a Fibonacci-like sequence based on user input. Unlike the standard Fibonacci sequence which starts with 0 and 1, this version allows the user to provide **custom starting values** (`a`, `b`) and the **number of terms** to generate.

> ⚠️ This product is proprietary and licensed. Unauthorized redistribution or resale is strictly prohibited.

## 📌 Features

- Input custom first two terms (`a` and `b`)
- Choose how many terms to generate
- Outputs the resulting sequence to the console

## 🧮 How It Works

The Fibonacci sequence is defined by the recurrence:

```
F(n) = F(n-1) + F(n-2)
```

With user-defined values:
- `F(0) = a`
- `F(1) = b`

Each subsequent number is the sum of the previous two.

## ▶️ Example

```
Enter the first term (a): 2
Enter the second term (b): 3
Enter the number of terms to generate: 7
Generated sequence:
2 3 5 8 13 21 34
```

## 🛠 Usage

1. Make sure you have Python installed.
2. Run the script:

```bash
python FibonacciGenerator.py
```

3. Enter the values as prompted.

## 📂 Files

```
CodeAlpha_VoiceAssistant/
│
├── FibonacciGenerator.py        # Main application script
├── LICENSE                      # Proprietary License
├── README.md                    # This file
```

## 📜 License

This software is licensed for individual or commercial use under a proprietary license. Redistribution, modification, or resale is **not permitted** without written authorization from the owner.

See [LICENSE](LICENSE) for full terms.

## 👨‍💻 Author

**Samith Mendis**  
GitHub: [@dsamithmendis](https://github.com/dsamithmendis)  
Email: [samithmendis.01@gmail.com]
