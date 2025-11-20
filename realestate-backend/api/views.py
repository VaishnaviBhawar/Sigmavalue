from rest_framework.response import Response
from rest_framework.decorators import api_view
import pandas as pd
import numpy as np

@api_view(['GET'])
def get_locations(request):
    df = pd.read_excel("./../Sample_data.xlsx")
    
    # Fix NaN for JSON
    df = df.replace({np.nan: None})

    return Response(df.to_dict(orient="records"))


@api_view(['POST'])
def analyze_location(request):
    data = request.data
    return Response({"message": "Location analyzed successfully!", "input": data})
