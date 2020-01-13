-- One to One
SELECT * FROM customers 
JOIN addresses ON addresses.id = customers.address_id;
-- One to Many
SELECT * FROM orders
JOIN customers ON  customers.id = orders.customer_id;
-- Many to Many
SELECT * FROM orders
JOIN items_orders ON orders.id = items_orders.order_id
JOIN items ON items.id = items_orders.item_id;