PRAGMA foreign_keys=OFF;
BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "django_migrations" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app" varchar(255) NOT NULL, "name" varchar(255) NOT NULL, "applied" datetime NOT NULL);
INSERT INTO django_migrations VALUES(1,'contenttypes','0001_initial','2020-05-22 04:46:15.275351');
INSERT INTO django_migrations VALUES(2,'auth','0001_initial','2020-05-22 04:46:15.437662');
INSERT INTO django_migrations VALUES(3,'admin','0001_initial','2020-05-22 04:46:15.564389');
INSERT INTO django_migrations VALUES(4,'admin','0002_logentry_remove_auto_add','2020-05-22 04:46:15.682738');
INSERT INTO django_migrations VALUES(5,'admin','0003_logentry_add_action_flag_choices','2020-05-22 04:46:15.813210');
INSERT INTO django_migrations VALUES(6,'contenttypes','0002_remove_content_type_name','2020-05-22 04:46:15.966699');
INSERT INTO django_migrations VALUES(7,'auth','0002_alter_permission_name_max_length','2020-05-22 04:46:16.092695');
INSERT INTO django_migrations VALUES(8,'auth','0003_alter_user_email_max_length','2020-05-22 04:46:16.223647');
INSERT INTO django_migrations VALUES(9,'auth','0004_alter_user_username_opts','2020-05-22 04:46:16.361016');
INSERT INTO django_migrations VALUES(10,'auth','0005_alter_user_last_login_null','2020-05-22 04:46:16.507080');
INSERT INTO django_migrations VALUES(11,'auth','0006_require_contenttypes_0002','2020-05-22 04:46:16.606815');
INSERT INTO django_migrations VALUES(12,'auth','0007_alter_validators_add_error_messages','2020-05-22 04:46:16.733190');
INSERT INTO django_migrations VALUES(13,'auth','0008_alter_user_username_max_length','2020-05-22 04:46:16.852364');
INSERT INTO django_migrations VALUES(14,'auth','0009_alter_user_last_name_max_length','2020-05-22 04:46:16.978231');
INSERT INTO django_migrations VALUES(15,'auth','0010_alter_group_name_max_length','2020-05-22 04:46:17.099008');
INSERT INTO django_migrations VALUES(16,'auth','0011_update_proxy_permissions','2020-05-22 04:46:17.226862');
INSERT INTO django_migrations VALUES(17,'beneficiaries','0001_initial','2020-05-22 04:46:17.335759');
INSERT INTO django_migrations VALUES(18,'collaborators','0001_initial','2020-05-22 04:46:17.444276');
INSERT INTO django_migrations VALUES(19,'projects','0001_initial','2020-05-22 04:46:17.636325');
INSERT INTO django_migrations VALUES(20,'sessions','0001_initial','2020-05-22 04:46:17.761690');
CREATE TABLE IF NOT EXISTS "auth_group_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE IF NOT EXISTS "auth_user_groups" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "group_id" integer NOT NULL REFERENCES "auth_group" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE IF NOT EXISTS "auth_user_user_permissions" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "permission_id" integer NOT NULL REFERENCES "auth_permission" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE IF NOT EXISTS "django_admin_log" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "action_time" datetime NOT NULL, "object_id" text NULL, "object_repr" varchar(200) NOT NULL, "change_message" text NOT NULL, "content_type_id" integer NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED, "user_id" integer NOT NULL REFERENCES "auth_user" ("id") DEFERRABLE INITIALLY DEFERRED, "action_flag" smallint unsigned NOT NULL CHECK ("action_flag" >= 0));
CREATE TABLE IF NOT EXISTS "django_content_type" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "app_label" varchar(100) NOT NULL, "model" varchar(100) NOT NULL);
INSERT INTO django_content_type VALUES(1,'admin','logentry');
INSERT INTO django_content_type VALUES(2,'auth','permission');
INSERT INTO django_content_type VALUES(3,'auth','group');
INSERT INTO django_content_type VALUES(4,'auth','user');
INSERT INTO django_content_type VALUES(5,'contenttypes','contenttype');
INSERT INTO django_content_type VALUES(6,'sessions','session');
INSERT INTO django_content_type VALUES(7,'collaborators','collaborator');
INSERT INTO django_content_type VALUES(8,'beneficiaries','beneficiary');
INSERT INTO django_content_type VALUES(9,'projects','project');
INSERT INTO django_content_type VALUES(10,'projects','projectcategory');
INSERT INTO django_content_type VALUES(11,'projects','projectstatus');
INSERT INTO django_content_type VALUES(12,'projects','taskcategory');
INSERT INTO django_content_type VALUES(13,'projects','task');
CREATE TABLE IF NOT EXISTS "auth_permission" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "content_type_id" integer NOT NULL REFERENCES "django_content_type" ("id") DEFERRABLE INITIALLY DEFERRED, "codename" varchar(100) NOT NULL, "name" varchar(255) NOT NULL);
INSERT INTO auth_permission VALUES(1,1,'add_logentry','Can add log entry');
INSERT INTO auth_permission VALUES(2,1,'change_logentry','Can change log entry');
INSERT INTO auth_permission VALUES(3,1,'delete_logentry','Can delete log entry');
INSERT INTO auth_permission VALUES(4,1,'view_logentry','Can view log entry');
INSERT INTO auth_permission VALUES(5,2,'add_permission','Can add permission');
INSERT INTO auth_permission VALUES(6,2,'change_permission','Can change permission');
INSERT INTO auth_permission VALUES(7,2,'delete_permission','Can delete permission');
INSERT INTO auth_permission VALUES(8,2,'view_permission','Can view permission');
INSERT INTO auth_permission VALUES(9,3,'add_group','Can add group');
INSERT INTO auth_permission VALUES(10,3,'change_group','Can change group');
INSERT INTO auth_permission VALUES(11,3,'delete_group','Can delete group');
INSERT INTO auth_permission VALUES(12,3,'view_group','Can view group');
INSERT INTO auth_permission VALUES(13,4,'add_user','Can add user');
INSERT INTO auth_permission VALUES(14,4,'change_user','Can change user');
INSERT INTO auth_permission VALUES(15,4,'delete_user','Can delete user');
INSERT INTO auth_permission VALUES(16,4,'view_user','Can view user');
INSERT INTO auth_permission VALUES(17,5,'add_contenttype','Can add content type');
INSERT INTO auth_permission VALUES(18,5,'change_contenttype','Can change content type');
INSERT INTO auth_permission VALUES(19,5,'delete_contenttype','Can delete content type');
INSERT INTO auth_permission VALUES(20,5,'view_contenttype','Can view content type');
INSERT INTO auth_permission VALUES(21,6,'add_session','Can add session');
INSERT INTO auth_permission VALUES(22,6,'change_session','Can change session');
INSERT INTO auth_permission VALUES(23,6,'delete_session','Can delete session');
INSERT INTO auth_permission VALUES(24,6,'view_session','Can view session');
INSERT INTO auth_permission VALUES(25,7,'add_collaborator','Can add collaborator');
INSERT INTO auth_permission VALUES(26,7,'change_collaborator','Can change collaborator');
INSERT INTO auth_permission VALUES(27,7,'delete_collaborator','Can delete collaborator');
INSERT INTO auth_permission VALUES(28,7,'view_collaborator','Can view collaborator');
INSERT INTO auth_permission VALUES(29,8,'add_beneficiary','Can add Beneficiary');
INSERT INTO auth_permission VALUES(30,8,'change_beneficiary','Can change Beneficiary');
INSERT INTO auth_permission VALUES(31,8,'delete_beneficiary','Can delete Beneficiary');
INSERT INTO auth_permission VALUES(32,8,'view_beneficiary','Can view Beneficiary');
INSERT INTO auth_permission VALUES(33,9,'add_project','Can add project');
INSERT INTO auth_permission VALUES(34,9,'change_project','Can change project');
INSERT INTO auth_permission VALUES(35,9,'delete_project','Can delete project');
INSERT INTO auth_permission VALUES(36,9,'view_project','Can view project');
INSERT INTO auth_permission VALUES(37,10,'add_projectcategory','Can add Project Category');
INSERT INTO auth_permission VALUES(38,10,'change_projectcategory','Can change Project Category');
INSERT INTO auth_permission VALUES(39,10,'delete_projectcategory','Can delete Project Category');
INSERT INTO auth_permission VALUES(40,10,'view_projectcategory','Can view Project Category');
INSERT INTO auth_permission VALUES(41,11,'add_projectstatus','Can add Project Status');
INSERT INTO auth_permission VALUES(42,11,'change_projectstatus','Can change Project Status');
INSERT INTO auth_permission VALUES(43,11,'delete_projectstatus','Can delete Project Status');
INSERT INTO auth_permission VALUES(44,11,'view_projectstatus','Can view Project Status');
INSERT INTO auth_permission VALUES(45,12,'add_taskcategory','Can add Task Category');
INSERT INTO auth_permission VALUES(46,12,'change_taskcategory','Can change Task Category');
INSERT INTO auth_permission VALUES(47,12,'delete_taskcategory','Can delete Task Category');
INSERT INTO auth_permission VALUES(48,12,'view_taskcategory','Can view Task Category');
INSERT INTO auth_permission VALUES(49,13,'add_task','Can add task');
INSERT INTO auth_permission VALUES(50,13,'change_task','Can change task');
INSERT INTO auth_permission VALUES(51,13,'delete_task','Can delete task');
INSERT INTO auth_permission VALUES(52,13,'view_task','Can view task');
CREATE TABLE IF NOT EXISTS "auth_user" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "password" varchar(128) NOT NULL, "last_login" datetime NULL, "is_superuser" bool NOT NULL, "username" varchar(150) NOT NULL UNIQUE, "first_name" varchar(30) NOT NULL, "email" varchar(254) NOT NULL, "is_staff" bool NOT NULL, "is_active" bool NOT NULL, "date_joined" datetime NOT NULL, "last_name" varchar(150) NOT NULL);
INSERT INTO auth_user VALUES(1,'pbkdf2_sha256$180000$XOvfrPZL8rD5$XjVynYzpycfIQjWIWPYSUVza9NTylaiH+xcFcwYHUKk=',NULL,1,'admin','','admin@adming.com',1,1,'2020-05-22 04:46:48.642018','');
CREATE TABLE IF NOT EXISTS "auth_group" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(150) NOT NULL UNIQUE);
CREATE TABLE IF NOT EXISTS "beneficiaries_beneficiary" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "first_name" varchar(30) NOT NULL, "last_name" varchar(30) NOT NULL, "age" integer NOT NULL, "sex" varchar(1) NOT NULL, "email" varchar(254) NOT NULL);
CREATE TABLE IF NOT EXISTS "collaborators_collaborator" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "first_name" varchar(30) NOT NULL, "last_name" varchar(30) NOT NULL, "age" integer NOT NULL, "sex" varchar(1) NOT NULL, "email" varchar(254) NOT NULL);
CREATE TABLE IF NOT EXISTS "projects_projectcategory" ("category" varchar(30) NOT NULL PRIMARY KEY, "description" varchar(60) NULL);
CREATE TABLE IF NOT EXISTS "projects_projectstatus" ("status" varchar(30) NOT NULL PRIMARY KEY, "description" varchar(60) NULL);
CREATE TABLE IF NOT EXISTS "projects_taskcategory" ("category" varchar(30) NOT NULL PRIMARY KEY, "description" varchar(60) NULL);
CREATE TABLE IF NOT EXISTS "projects_task" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(30) NULL, "due" datetime NOT NULL, "description" varchar(60) NULL, "category_id" varchar(30) NOT NULL REFERENCES "projects_taskcategory" ("category") DEFERRABLE INITIALLY DEFERRED, "project_id" integer NOT NULL REFERENCES "projects_project" ("id") DEFERRABLE INITIALLY DEFERRED, "responsable_id" integer NOT NULL REFERENCES "collaborators_collaborator" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE IF NOT EXISTS "projects_project_collaborators" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "project_id" integer NOT NULL REFERENCES "projects_project" ("id") DEFERRABLE INITIALLY DEFERRED, "collaborator_id" integer NOT NULL REFERENCES "collaborators_collaborator" ("id") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE IF NOT EXISTS "projects_project" ("id" integer NOT NULL PRIMARY KEY AUTOINCREMENT, "name" varchar(60) NULL, "description" varchar(120) NULL, "direction" varchar(120) NULL, "category_id" varchar(30) NOT NULL REFERENCES "projects_projectcategory" ("category") DEFERRABLE INITIALLY DEFERRED, "status_id" varchar(30) NOT NULL REFERENCES "projects_projectstatus" ("status") DEFERRABLE INITIALLY DEFERRED);
CREATE TABLE IF NOT EXISTS "django_session" ("session_key" varchar(40) NOT NULL PRIMARY KEY, "session_data" text NOT NULL, "expire_date" datetime NOT NULL);
DELETE FROM sqlite_sequence;
INSERT INTO sqlite_sequence VALUES('django_migrations',20);
INSERT INTO sqlite_sequence VALUES('django_admin_log',0);
INSERT INTO sqlite_sequence VALUES('django_content_type',13);
INSERT INTO sqlite_sequence VALUES('auth_permission',52);
INSERT INTO sqlite_sequence VALUES('auth_user',1);
INSERT INTO sqlite_sequence VALUES('auth_group',0);
INSERT INTO sqlite_sequence VALUES('projects_project',0);
CREATE UNIQUE INDEX "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" ON "auth_group_permissions" ("group_id", "permission_id");
CREATE INDEX "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" ("group_id");
CREATE INDEX "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" ("permission_id");
CREATE UNIQUE INDEX "auth_user_groups_user_id_group_id_94350c0c_uniq" ON "auth_user_groups" ("user_id", "group_id");
CREATE INDEX "auth_user_groups_user_id_6a12ed8b" ON "auth_user_groups" ("user_id");
CREATE INDEX "auth_user_groups_group_id_97559544" ON "auth_user_groups" ("group_id");
CREATE UNIQUE INDEX "auth_user_user_permissions_user_id_permission_id_14a6b632_uniq" ON "auth_user_user_permissions" ("user_id", "permission_id");
CREATE INDEX "auth_user_user_permissions_user_id_a95ead1b" ON "auth_user_user_permissions" ("user_id");
CREATE INDEX "auth_user_user_permissions_permission_id_1fbb5f2c" ON "auth_user_user_permissions" ("permission_id");
CREATE INDEX "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" ("content_type_id");
CREATE INDEX "django_admin_log_user_id_c564eba6" ON "django_admin_log" ("user_id");
CREATE UNIQUE INDEX "django_content_type_app_label_model_76bd3d3b_uniq" ON "django_content_type" ("app_label", "model");
CREATE UNIQUE INDEX "auth_permission_content_type_id_codename_01ab375a_uniq" ON "auth_permission" ("content_type_id", "codename");
CREATE INDEX "auth_permission_content_type_id_2f476e4b" ON "auth_permission" ("content_type_id");
CREATE INDEX "projects_task_category_id_e9b54027" ON "projects_task" ("category_id");
CREATE INDEX "projects_task_project_id_a1b987d6" ON "projects_task" ("project_id");
CREATE INDEX "projects_task_responsable_id_ffb8fe62" ON "projects_task" ("responsable_id");
CREATE UNIQUE INDEX "projects_project_collaborators_project_id_collaborator_id_390ae020_uniq" ON "projects_project_collaborators" ("project_id", "collaborator_id");
CREATE INDEX "projects_project_collaborators_project_id_daa51cf3" ON "projects_project_collaborators" ("project_id");
CREATE INDEX "projects_project_collaborators_collaborator_id_4a2da90d" ON "projects_project_collaborators" ("collaborator_id");
CREATE INDEX "projects_project_category_id_708edb98" ON "projects_project" ("category_id");
CREATE INDEX "projects_project_status_id_9f58ac46" ON "projects_project" ("status_id");
CREATE INDEX "django_session_expire_date_a5c62663" ON "django_session" ("expire_date");
COMMIT;
