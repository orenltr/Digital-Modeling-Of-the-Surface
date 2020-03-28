import vtk

# Rendering a cube #

# Generate polygon data for a cube
cube = vtk.vtkCubeSource()

# Update the cube source (initialize the object class)
cube.Update()

# Create a mapper for the cube data
cube_mapper = vtk.vtkPolyDataMapper()
cube_mapper.SetInputData(cube.GetOutput())

# Connect the mapper to an actor
cube_actor = vtk.vtkActor()
cube_actor.SetMapper(cube_mapper)
cube_actor.GetProperty().SetColor(1.0, 0.0, 0.0)

# Create a renderer and add the cube actor to it
renderer = vtk.vtkRenderer()
renderer.SetBackground(0.0 , 0.0 , 0.0)
renderer.AddActor(cube_actor)
renderer.ResetCamera()

# Create a render window
render_window = vtk.vtkRenderWindow()
render_window.SetWindowName('Simple VTK')
render_window.SetSize(400 , 400)
render_window.AddRenderer(renderer)

# Create an interactor
interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(render_window)

# Initialize the interactor and start the
# rendering loop
interactor.Initialize()
render_window.Render()
interactor.Start()

# Point cloud rendering #

# Create source
pnt = vtk.vtkPointSource()
pnt.SetCenter(0 , 0 , 0)

# Set number of point in the point cloud to be
# rendered in an unit sphere (radius = 1.0)
pnt.SetNumberOfPoints(1000)

# Set sphere radius to 5
pnt.SetRadius(5)

# Update the source, i.e., p nt
# (initialize the object class)
pnt.Update()

# Mapper
mapper = vtk.vtkPolyDataMapper()
mapper.SetInputConnection(pnt.GetOutputPort())

# Actor
actor = vtk.vtkActor()
actor.SetMapper(mapper)

# create a rendering window and renderer
renderer = vtk.vtkRenderer()
render_window = vtk.vtkRenderWindow()
render_window.AddRenderer(renderer)

# Assign actor to the renderer
renderer.AddActor(actor)

# create a rendering window and renderer
renderer = vtk.vtkRenderer()
render_window = vtk.vtkRenderWindow()
render_window.AddRenderer(renderer)

# Assign actor to the renderer
renderer.AddActor(actor)

# create a renderwindowinteractor
interactor = vtk.vtkRenderWindowInteractor()
interactor.SetRenderWindow(render_window)

# Enable user interface interactor
interactor.Initialize()
render_window.Render()
interactor.Start()