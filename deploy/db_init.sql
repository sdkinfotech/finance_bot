CREATE DATABASE expenses_income_db;

-- Создание таблицы expenses
CREATE TABLE IF NOT EXISTS expenses (
    id SERIAL PRIMARY KEY,
    date DATE NOT NULL,
    time TIME WITHOUT TIME ZONE NOT NULL,
    category TEXT NOT NULL,
    description TEXT,
    amount NUMERIC(10, 2) NOT NULL CHECK (amount > 0),
    currency CHAR(3) NOT NULL DEFAULT 'RUB'
);

-- Создание триггера для автоматической установки времени и даты для таблицы expenses
CREATE OR REPLACE FUNCTION set_expenses_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.date = CURRENT_DATE;
    NEW.time = CURRENT_TIME;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER expenses_before_insert
BEFORE INSERT ON expenses
FOR EACH ROW EXECUTE FUNCTION set_expenses_timestamp();

-- Создание триггера для автоматической установки времени и даты для таблицы income
CREATE OR REPLACE FUNCTION set_income_timestamp()
RETURNS TRIGGER AS $$
BEGIN
    NEW.date = CURRENT_DATE;
    NEW.time = CURRENT_TIME;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

CREATE TRIGGER income_before_insert
BEFORE INSERT ON income
FOR EACH ROW EXECUTE FUNCTION set_income_timestamp();