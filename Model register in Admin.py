admin.site.register(rates)


@admin.register(rates)
class ratesAdmin(admin.ModelAdmin):
  list_display = ('id', 'name', 'rate')

