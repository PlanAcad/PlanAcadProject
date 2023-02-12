/****** Script for SelectTopNRows command from SSMS  ******/
SET IDENTITY_INSERT [dbo].[auth_group] ON
INSERT INTO [dbo].[auth_group] (id, name)
VALUES (1, 'profesor' ),
       (2, 'alumno' ),
	   (3, 'jefe de carrera' ),
       (4, 'consejo');
SET IDENTITY_INSERT [dbo].[auth_group] OFF 