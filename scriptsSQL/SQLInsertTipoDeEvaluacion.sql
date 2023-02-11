/****** Script for SelectTopNRows command from SSMS  ******/

SET IDENTITY_INSERT [dbo].[planificaciones_tipodeevaluacion] ON
INSERT INTO [dbo].[planificaciones_tipodeevaluacion] (id, tipo)
VALUES (1,'D' ),
       (2,'F' ),
	   (3,'S'),
	   (4,'SF');
SET IDENTITY_INSERT [dbo].[planificaciones_tipodeevaluacion] OFF 