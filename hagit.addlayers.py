import rhinoscriptsyntax as rs
import scriptcontext as sc
import Rhino
sc.doc = Rhino.RhinoDoc.ActiveDoc

if y==True:
    rs.AddLayer(name=x)
