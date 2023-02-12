/****** Script for SelectTopNRows command from SSMS  ******/

  
SET IDENTITY_INSERT [dbo].[planificaciones_situacion] ON
INSERT INTO [dbo].[planificaciones_situacion] (id, situacion)
VALUES (2, 'CONC' ),
       (3, 'INT');
SET IDENTITY_INSERT [dbo].[planificaciones_situacion] OFF 