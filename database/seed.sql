INSERT OR IGNORE INTO customers VALUES
(1, 'Ravi', 'Male', 'Bangalore', 'Karnataka'),
(2, 'Priya', 'Female', 'Mysore', 'Karnataka'),
(3, 'Arun', 'Male', 'Kolar', 'Karnataka'),
(4, 'Sneha', 'Female', 'Bangalore', 'Karnataka'),
(5, 'Kiran', 'Male', 'Tumkur', 'Karnataka'),
(6, 'Anu', 'Female', 'Chennai', 'Tamil Nadu'),
(7, 'Rahul', 'Male', 'Hyderabad', 'Telangana'),
(8, 'Divya', 'Female', 'Mangalore', 'Karnataka');

INSERT OR IGNORE INTO products VALUES
(101, 'Laptop', 'Electronics', 55000),
(102, 'Mobile', 'Electronics', 25000),
(103, 'Headphones', 'Accessories', 2000),
(104, 'Keyboard', 'Accessories', 1500),
(105, 'Mouse', 'Accessories', 800),
(106, 'Monitor', 'Electronics', 12000),
(107, 'Smart Watch', 'Wearables', 5000),
(108, 'Tablet', 'Electronics', 18000);

INSERT OR IGNORE INTO orders VALUES
(1001, 1, '2026-09-01', 'UPI', 'Delivered'),
(1002, 2, '2026-09-02', 'Card', 'Delivered'),
(1003, 3, '2026-09-03', 'Cash', 'Pending'),
(1004, 4, '2026-09-04', 'UPI', 'Delivered'),
(1005, 5, '2026-09-05', 'Card', 'Cancelled'),
(1006, 6, '2026-09-06', 'UPI', 'Delivered'),
(1007, 7, '2026-09-07', 'Card', 'Delivered'),
(1008, 8, '2026-09-08', 'UPI', 'Pending'),
(1009, 1, '2026-09-10', 'Card', 'Delivered'),
(1010, 2, '2026-09-11', 'UPI', 'Delivered');

INSERT OR IGNORE INTO order_details VALUES
(1, 1001, 101, 1, 55000),
(2, 1002, 102, 2, 25000),
(3, 1003, 103, 3, 2000),
(4, 1004, 101, 1, 55000),
(5, 1005, 105, 2, 800),
(6, 1006, 106, 1, 12000),
(7, 1007, 107, 2, 5000),
(8, 1008, 108, 1, 18000),
(9, 1009, 104, 2, 1500),
(10, 1010, 102, 1, 25000);
