from population import Population

class Location:
  def __init__(self, name, coords, extent, populations, container):
    self.name=name
    self.coords=coords
    self.extent=extent
    self.container=container
    self.populations=populations
