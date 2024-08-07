SELECT
	category.category_name AS category_name,
    SUM(sale.sales) AS total_quantity
FROM
	category INNER JOIN order_sale ON (category.id_category = order_sale.category_id_category)
    INNER JOIN sale ON (sale.id_sale = order_sale.sale_id_sale)
GROUP BY
	category_name
ORDER BY
	total_quantity DESC;