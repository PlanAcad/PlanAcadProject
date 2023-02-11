/****** Script for SelectTopNRows command from SSMS  ******/

SET IDENTITY_INSERT [dbo].[planificaciones_dedicacion] ON
INSERT INTO [dbo].[planificaciones_dedicacion] (id, dedicacion)
VALUES (1, '1DS' ),
       (2, '2DS' ),
	   (3, '3DS' ),
	   (4, 'Exclusiva' );
SET IDENTITY_INSERT [dbo].[planificaciones_dedicacion] OFF 