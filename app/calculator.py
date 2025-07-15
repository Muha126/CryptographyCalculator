"""Calculation and controll"""
from functools import partial
ERROR_MSG = "ERROR!"


def evaluateExpression(expression):
    """Evaluate expression"""
    try:
        result = str(eval(expression, {}, {}))
    except Exception:
        result = ERROR_MSG
    return result


class PyCalc:
    """Controllers class"""

    def __init__(self,model,view):
        self._evaluate = model
        self._view = view
        self._connectSignalsAndSlots()

    
    def calculateResult(self):
        self._view.trigger()
        result = self._evaluate(expression=self._view.displayText())
        self._view.setDisplayText(result)
        

    
    def _buildExpression(self, subExpression):
        if self._view.displayText() == ERROR_MSG:
            self._view.clearDisplay()
        expression = self._view.displayText() + subExpression
        self._view.setDisplayText(expression)

    
    def _connectSignalsAndSlots(self):
        for keySymbol, button in self._view.buttonMap.items():
            if keySymbol not in {"=", "C"}:
                button.clicked.connect(
                    partial(self._buildExpression, keySymbol)
                )
        self._view.buttonMap["="].clicked.connect(self.calculateResult)
        self._view.display.returnPressed.connect(self.calculateResult)
        self._view.buttonMap["C"].clicked.connect(self._view.clearDisplay)

