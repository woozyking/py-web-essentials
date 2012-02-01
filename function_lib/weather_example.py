import weather

dom_obj = get_weather( 'mcmaster university', 'ar' )
xml_str = dom_obj.toprettyxml()

print xml_str
