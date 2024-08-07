SELECT
	customer.id_customer AS customer_id,
    customer.customer_name AS customer_name,
    COUNT(order_sale.id_order) AS num_orders
FROM
	customer LEFT JOIN order_sale ON (customer.id_customer = order_sale.customer_id_customer)
GROUP BY
	customer_id, customer_name
ORDER BY
	customer_id;
    
SELECT count(*)
FROM customer;