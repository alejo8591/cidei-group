BEGIN;
CREATE TABLE `django_admin_log` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `action_time` datetime NOT NULL,
    `user_id` integer NOT NULL,
    `content_type_id` integer,
    `object_id` longtext,
    `object_repr` varchar(200) NOT NULL,
    `action_flag` smallint UNSIGNED NOT NULL,
    `change_message` longtext NOT NULL
)
;
-- The following references should be added but depend on non-existent tables:
-- ALTER TABLE `django_admin_log` ADD CONSTRAINT `content_type_id_refs_id_93d2d1f8` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);
-- ALTER TABLE `django_admin_log` ADD CONSTRAINT `user_id_refs_id_c0d12874` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
CREATE INDEX `django_admin_log_6340c63c` ON `django_admin_log` (`user_id`);
CREATE INDEX `django_admin_log_37ef4eb4` ON `django_admin_log` (`content_type_id`);

COMMIT;

BEGIN;
CREATE TABLE `auth_permission` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` varchar(50) NOT NULL,
    `content_type_id` integer NOT NULL,
    `codename` varchar(100) NOT NULL,
    UNIQUE (`content_type_id`, `codename`)
)
;
CREATE TABLE `auth_group_permissions` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `group_id` integer NOT NULL,
    `permission_id` integer NOT NULL,
    UNIQUE (`group_id`, `permission_id`)
)
;
ALTER TABLE `auth_group_permissions` ADD CONSTRAINT `permission_id_refs_id_6ba0f519` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);
CREATE TABLE `auth_group` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` varchar(80) NOT NULL UNIQUE
)
;
ALTER TABLE `auth_group_permissions` ADD CONSTRAINT `group_id_refs_id_f4b32aac` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);
CREATE TABLE `auth_user_groups` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `user_id` integer NOT NULL,
    `group_id` integer NOT NULL,
    UNIQUE (`user_id`, `group_id`)
)
;
ALTER TABLE `auth_user_groups` ADD CONSTRAINT `group_id_refs_id_274b862c` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);
CREATE TABLE `auth_user_user_permissions` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `user_id` integer NOT NULL,
    `permission_id` integer NOT NULL,
    UNIQUE (`user_id`, `permission_id`)
)
;
ALTER TABLE `auth_user_user_permissions` ADD CONSTRAINT `permission_id_refs_id_35d9ac25` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);
CREATE TABLE `auth_user` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `password` varchar(128) NOT NULL,
    `last_login` datetime NOT NULL,
    `is_superuser` bool NOT NULL,
    `username` varchar(30) NOT NULL UNIQUE,
    `first_name` varchar(30) NOT NULL,
    `last_name` varchar(30) NOT NULL,
    `email` varchar(75) NOT NULL,
    `is_staff` bool NOT NULL,
    `is_active` bool NOT NULL,
    `date_joined` datetime NOT NULL
)
;

CREATE TABLE `django_admin_log` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `action_time` datetime NOT NULL,
    `user_id` integer NOT NULL,
    `content_type_id` integer,
    `object_id` longtext,
    `object_repr` varchar(200) NOT NULL,
    `action_flag` smallint UNSIGNED NOT NULL,
    `change_message` longtext NOT NULL
)
;

CREATE TABLE `django_session` (
    `session_key` varchar(40) NOT NULL PRIMARY KEY,
    `session_data` longtext NOT NULL,
    `expire_date` datetime NOT NULL
)
;

CREATE TABLE `django_content_type` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` varchar(100) NOT NULL,
    `app_label` varchar(100) NOT NULL,
    `model` varchar(100) NOT NULL,
    UNIQUE (`app_label`, `model`)
)
;




ALTER TABLE `auth_user_groups` ADD CONSTRAINT `user_id_refs_id_40c41112` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
ALTER TABLE `auth_user_user_permissions` ADD CONSTRAINT `user_id_refs_id_4dc23c39` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
-- The following references should be added but depend on non-existent tables:
-- ALTER TABLE `auth_permission` ADD CONSTRAINT `content_type_id_refs_id_d043b34a` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);
CREATE INDEX `auth_permission_37ef4eb4` ON `auth_permission` (`content_type_id`);
CREATE INDEX `auth_group_permissions_5f412f9a` ON `auth_group_permissions` (`group_id`);
CREATE INDEX `auth_group_permissions_83d7f98b` ON `auth_group_permissions` (`permission_id`);
CREATE INDEX `auth_user_groups_6340c63c` ON `auth_user_groups` (`user_id`);
CREATE INDEX `auth_user_groups_5f412f9a` ON `auth_user_groups` (`group_id`);
CREATE INDEX `auth_user_user_permissions_6340c63c` ON `auth_user_user_permissions` (`user_id`);
CREATE INDEX `auth_user_user_permissions_83d7f98b` ON `auth_user_user_permissions` (`permission_id`);

-- The following references should be added but depend on non-existent tables: 
-- ALTER TABLE `django_admin_log` ADD CONSTRAINT `content_type_id_refs_id_93d2d1f8` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);
-- ALTER TABLE `django_admin_log` ADD CONSTRAINT `user_id_refs_id_c0d12874` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
CREATE INDEX `django_admin_log_6340c63c` ON `django_admin_log` (`user_id`);
CREATE INDEX `django_admin_log_37ef4eb4` ON `django_admin_log` (`content_type_id`);       

CREATE INDEX `django_session_b7b81f0c` ON `django_session` (`expire_date`);


CREATE TABLE `sales_categories` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` varchar(255) NOT NULL,
    `description` longtext,
    `picture` varchar(100) NOT NULL,
    `posted_on` datetime NOT NULL
)
;
CREATE TABLE `sales_suppliers` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` varchar(255) NOT NULL,
    `description` longtext,
    `address` varchar(255) NOT NULL,
    `phone` varchar(12) NOT NULL,
    `posted_on` datetime NOT NULL
)
;
CREATE TABLE `sales_products` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `name` varchar(255) NOT NULL,
    `value` integer UNSIGNED NOT NULL,
    `category_id` integer NOT NULL,
    `supplier_id` integer NOT NULL,
    `unit_price` integer UNSIGNED NOT NULL,
    `units_in_stock` integer UNSIGNED NOT NULL,
    `discontinued` bool NOT NULL,
    `posted_on` datetime NOT NULL
)
;
ALTER TABLE `sales_products` ADD CONSTRAINT `category_id_refs_id_1e4bc9a0` FOREIGN KEY (`category_id`) REFERENCES `sales_categories` (`id`);
ALTER TABLE `sales_products` ADD CONSTRAINT `supplier_id_refs_id_a652f23a` FOREIGN KEY (`supplier_id`) REFERENCES `sales_suppliers` (`id`);
CREATE TABLE `sales_orders` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `description` longtext,
    `created_on` datetime NOT NULL
)
;
CREATE TABLE `sales_orderdetail` (
    `id` integer AUTO_INCREMENT NOT NULL PRIMARY KEY,
    `order_id` integer NOT NULL,
    `quantity` integer UNSIGNED NOT NULL,
    `discount` integer UNSIGNED NOT NULL,
    `created_on` datetime NOT NULL
)
;
ALTER TABLE `sales_orderdetail` ADD CONSTRAINT `order_id_refs_id_2fddb8b0` FOREIGN KEY (`order_id`) REFERENCES `sales_orders` (`id`);
CREATE INDEX `sales_products_6f33f001` ON `sales_products` (`category_id`);
CREATE INDEX `sales_products_272520ac` ON `sales_products` (`supplier_id`);
CREATE INDEX `sales_orderdetail_68d25c7a` ON `sales_orderdetail` (`order_id`);

COMMIT;
