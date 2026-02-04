use its2026;

insert into products (code, name, description, price, quantity) values 
('PRD00001', 'Pasta integrale', 'Pasta di grano duro 100% ingrale 500Kg', 1.49, 100);
insert into products (code, name, description, price, quantity) values 
('PRD00002', 'Olio extravergine', 'Olio extravergine d\oliva 750ml', 6.90, 50);
insert into products (code, name, description, price, quantity) values 
('PRD00003', 'Biscotti al cacao', 'Biscotti secchi con gocce di cioccolato', 2.75, 80);
insert into products (code, name, description, price, quantity) values 
('PRD00004', 'Passata di pomodoro', 'Passata di pomodoro biologica 700g', 1.29, 90); 
#cambio a 90 invece che 120 perché qauntity supporta fino a 100
insert into products (code, name, description, price, quantity) values 
('PRD00005', 'Riso basmati', 'Riso basmati confezione da 1kg', 3.10, 60);

insert into orders (order_data, total, shipping, shipping_address, customer_id) values
('2025-06-01', 25.38, 'shipped', 'Via Roma 12 Milano', 101), ('2025-06-02', 47.20, 'delivered', 'Corso Italia 45 Torino', 102), 
();



