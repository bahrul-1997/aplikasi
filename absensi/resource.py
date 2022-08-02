from import_export import resources
from .models import Mabsen
from import_export.fields import Field


class AbsenResource(resources.ModelResource):
    guru__id = Field(attribute='guru_id', column_name='Nama Guru')

    class Meta:
        model = Mabsen
        fields = ['guru__id', 'jam_masuk', 'keterangan']
