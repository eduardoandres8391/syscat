#Autogenerated by ReportLab guiedit do not edit
from reportlab.graphics.charts.piecharts import LegendedPie
from reportlab.graphics.shapes import _DrawingEditorMixin
from rlextra.graphics.guiedit.datacharts import CSVDataSource, ODBCDataSource, DataAssociation, DataAwareDrawing

class LegendedPieDrawing(_DrawingEditorMixin,DataAwareDrawing):
	def __init__(self,width=400,height=200,*args,**kw):
		DataAwareDrawing.__init__(self,width,height,*args,**kw)
		self._add(self,LegendedPie(),name='chart',validate=None,desc='The main chart')
		self.height = 110
		self.width = 200
		self.dataSource = CSVDataSource()
		self.dataSource.filename = 'legendedpie.csv'
		self.dataSource.sep = '\t'
		self.dataSource.sql = 'SELECT chartID,sliceId,name,value FROM generic_pie'
		self.dataSource.groupingColumn = 'chartId'
		self.dataSource.integerColumns = ['chartId']
		self.dataSource.floatColumns = ['value']
		self.dataSource.associations.size      = 4
		self.dataSource.groupingColumn         = 0
		self.dataSource.associations.element00 = DataAssociation(column=0, target='chartId', assocType='scalar')
		self.dataSource.associations.element01 = DataAssociation(column=3, target='chart.data', assocType='vector')
		self.dataSource.associations.element02 = DataAssociation(column=2, target='chart.legend_names', assocType='vector')
		self.dataSource.associations.element03 = DataAssociation(column=3, target='chart.legend_data', assocType='vector')
		self.fileNamePattern = 'piechart%03d'
		self.formats         = ['eps','pdf']
		self.verbose         = 1
		self.outDir          = './output/'


if __name__=="__main__": #NORUNTESTS
	LegendedPieDrawing().go()