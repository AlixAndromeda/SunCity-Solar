def calculateSavings():
    bill = float(Element("current-bill").element.value)
    rate = float(Element("savings-rate").element.value)
    savings = bill * (rate / 100)
    Element("result").element.innerText = f"Your estimated savings: ${savings:.2f} per month."
