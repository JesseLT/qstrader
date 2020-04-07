from .base import AbstractPositionSizer


class FixedPositionSizer(AbstractPositionSizer):
    def __init__(self, default_quantity=100):
        self.default_quantity = default_quantity

    def size_order(self, portfolio, initial_order):
        """
        This FixedPositionSizer object simply modifies
        the quantity to be 100 of any share transacted.
        """
        # initial_order.quantity = self.default_quantity
        """
        均仓购买
        """
        tickers = initial_order.ticker
        if initial_order.action=="SLD":
            initial_order.quantity = portfolio.positions[tickers].quantity
        else:
            fill_price = portfolio.price_handler.get_last_close(tickers)
            equity = portfolio.equity
            lt = len(portfolio.price_handler.tickers)
            initial_order.quantity = (equity//lt)//(fill_price*100)*100
        return initial_order
