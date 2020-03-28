import vtk
import numpy as np
import csv
import pandas as pd

# Mesh rendering #


# Read data
data= pd.read_csv('תרגיל בית 1 - קובץ נקודות.csv')
pnt = np.array(data)
data= pd.read_csv('תרגיל בית 1 - קובץ משולשים.csv')
tri = np.array(data)

# Initialize VTK points object
vtkPnt = vtk.vtkPoints()

# Initialize color scalars
pnt_rgb = vtk.vtkUnsignedCharArray()

# R, G, B
pnt_rgb.SetNumberOfComponents(3)

# Colors??
pnt_rgb.SetName('Colors')

# Initialize VTK PolyData object for vertices
vtkVertex = vtk.vtkPolyData()

# Initialize VTK PolyData object for triangulation
vtkTri = vtk.vtkPolyData()

# Initialize VTK vertices object for points
vtkVertex_ind = vtk.vtkCellArray()

# Initialize VTK vertices object for triangles
vtkTri_ind = vtk.vtkCellArray()

for i in range(pnt.shape[0]):
    # Inserting the i-th point to the vtkPoints object
    id = vtkPnt.InsertNextPoint(pnt[i, 0],
                                pnt[i, 1], pnt[i, 2])

    # Adding color for the i th point
    # pnt_rgb.InsertNextTupleValue(pnt[i, 3],
    #                              pnt[i, 4], pnt[i, 5])
    pnt_rgb.InsertNextTypedTuple((int(pnt[i, 3]),
                                 int(pnt[i, 4]), int(pnt[i, 5])))

    # Adding the index of i th point to vertex vtk
    # index array
    vtkVertex_ind.InsertNextCell(1)
    vtkVertex_ind.InsertCellPoint(id)

# Set vtk point in triangle polydata object
vtkTri.SetPoints(vtkPnt)

# Add color to the vtkTri object
vtkTri.GetPointData().SetScalars(pnt_rgb)

# Set vtk point in vertexes polydata object
vtkVertex.SetPoints(vtkPnt)
vtkVertex.SetVerts(vtkVertex_ind)

# Add color to the vtkVertex object
vtkVertex.GetPointData().SetScalars(pnt_rgb)

for i in range(tri.shape[0]):
    # Set triangle's 3 vertices by ID
    ith_tri = vtk.vtkTriangle()
    ith_tri.GetPointIds().SetId(0 , int(tri[ i , 0]))
    ith_tri.GetPointIds().SetId(1 , int(tri[ i , 1]))
    ith_tri.GetPointIds().SetId(2 , int(tri[ i , 2]))

    # Insert the i th triangle data index
    vtkTri_ind.InsertNextCell(ith_tri)

# Initialize a VTK mapper
vtkMapper = vtk.vtkPolyDataMapper()
vtkMapper.SetInputData(vtkVertex)
vtkTri.SetPolys(vtkTri_ind)
vtkMapper.SetInputData(vtkTri)

# Initialize a VTK actor
vtkActor = vtk.vtkActor()
vtkActor.SetMapper(vtkMapper)

# Initialize a VTK render window
vtkRenderWindow = vtk.vtkRenderWindow()

# Initialize a VTK renderer.
# Contains the actors to render
vtkRenderer = vtk.vtkRenderer()
# Add the VTK renderer to the VTK render window
vtkRenderWindow.AddRenderer(vtkRenderer)
# define the renderer
vtkRenderer.AddActor(vtkActor)

# Set camera and background data
vtkRenderer.ResetCamera()
vtkRenderWindow.Render()
# Enable user interface interactor
interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(vtkRenderWindow)
vtkRenderWindow.Render()
interactor.Start()
