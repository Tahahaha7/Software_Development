.mode column
.headers on
PRAGMA foreign_keys = ON;

CREATE TABLE Stocks ( 
    StockID INTEGER PRIMARY KEY,
    TickerSymbol TEXT,
    Value NUMERIC(10,2)
  );

CREATE TABLE Trader (
    TraderID INTEGER PRIMARY KEY,
    Portfolio INT
);

CREATE TABLE TradingHistory(
    TradeID INTEGER PRIMARY KEY,
    DateTrading DATETIME,
    TickerSymbol TEXT,
    FOREIGN KEY (TraderID) REFERENCES Stocks(StockID),
)

INSERT INTO Stocks VALUES (1, "GOOG", 23.05);
INSERT INTO Stocks VALUES (2, "XOM", 123.05);
INSERT INTO Stocks VALUES (3, "AAPL", 199.95);
INSERT INTO Stocks VALUES (4, "INTC", 75.22);
INSERT INTO Stocks VALUES (5, "WMT", 87.05);

INSERT INTO Trader VALUES (1, 2000);
INSERT INTO Trader VALUES (2, 5423);
INSERT INTO Trader VALUES (3, 6654);
INSERT INTO Trader VALUES (4, 6544);
INSERT INTO Trader VALUES (5, 9875);

INSERT INTO TradingHistory VALUES (9999, "2025-01-01 10:00:00", "AMZ");
INSERT INTO TradingHistory VALUES (1001, "2025-01-01 11:00:00", "AAPL");
INSERT INTO TradingHistory VALUES (1002, "2025-01-01 12:00:00", "WMT");

BEGIN TRANSACTION;
INSERT INTO TradingHistory VALUES (1000, "2025-01-01 10:00:00", "GOOG");
UPDATE Trader SET Portfolio = Portfolio - 100.00 WHERE TraderID = 1;
UPDATE Trader SET Portfolio = Portfolio + 100.00 WHERE TraderID = 2;
COMMIT;