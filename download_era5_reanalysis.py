import subprocess

from joblib import Parallel, delayed

apikey = '' # put here your key

def call(year):
    
    subprocess.run(f'echo -e "url: https://cds.climate.copernicus.eu/api/v2 \nkey: {apikey}" > $HOME/.cdsapirc; cat $HOME/.cdsapirc', shell=True, check=True, executable='/bin/bash')

    import cdsapi

    c = cdsapi.Client()

    specs = {
            'product_type': 'reanalysis',
            'format': 'netcdf',#'grib',
            'variable': [
                '100m_u_component_of_wind', '100m_v_component_of_wind',
                '10m_u_component_of_wind', '10m_v_component_of_wind',
                '2m_temperature', '2m_dewpoint_temperature', 'surface_pressure', 'total_precipitation',
                'geopotential', 'medium_cloud_cover'
            ],
            'year': [
                year
            ],
            'month': [
                '01', '02', '03',
                '04', '05', '06',
                '07', '08', '09',
                '10', '11', '12',
            ],
            'day': [
                '01', '02', '03',
                '04', '05', '06',
                '07', '08', '09',
                '10', '11', '12',
                '13', '14', '15',
                '16', '17', '18',
                '19', '20', '21',
                '22', '23', '24',
                '25', '26', '27',
                '28', '29', '30',
                '31',
            ],
            'time': [
                '00:00', '01:00', 
                '02:00', '03:00', 
                '04:00', '05:00',
                '06:00', '07:00', 
                '08:00', '09:00', 
                '10:00', '11:00',
                '12:00', '13:00', 
                '14:00', '15:00',
                '16:00', '17:00',
                '18:00', '19:00', 
                '20:00', '21:00', 
                '22:00', '23:00',
            ],
            'area': [
                48, 
                6, 
                36,
                19,
            ],
            'grid': [ # degree resolution
                1.0, 
                1.0
            ]
    }
    c.retrieve('reanalysis-era5-single-levels', specs, f'10vars/italy_era5_hourly_{year}_10vars.nc')#.grib
    return True

years = [str(y) for y in list(range(2003, 2024, 1))]
Parallel(n_jobs=len(years))(delayed(call)(y) for y in years)
