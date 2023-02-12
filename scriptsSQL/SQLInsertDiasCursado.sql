/****** Script for SelectTopNRows command from SSMS  ******/

SET IDENTITY_INSERT [dbo].[planificaciones_diascursado] ON
INSERT INTO [dbo].[planificaciones_diascursado] (id, dia)
VALUES (1, 'Lunes' ),
       (2, 'Martes' ),
	   (3, 'Miercoles' ),
	   (4, 'Jueves' ),
	   (5, 'Viernes' ),
       (6, 'Sabado');
SET IDENTITY_INSERT [dbo].[planificaciones_diascursado] OFF 
