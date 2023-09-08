import pandera as pa
from pandera.typing import Series

class SchemaTrain(pa.DataFrameModel):
    id: Series[int] = pa.Field(nullable=False)
    no_of_adults: Series[int] = pa.Field(nullable=False)
    no_of_children: Series[int] = pa.Field(nullable=False)
    no_of_weekend_nights: Series[int] = pa.Field(nullable=False)   
    no_of_week_nights: Series[int] = pa.Field(nullable=False)
    type_of_meal_plan: Series[int] = pa.Field(nullable=False)
    required_car_parking_space: Series[int] = pa.Field(nullable=False)
    room_type_reserved: Series[int] = pa.Field(nullable=False)
    lead_time: Series[int] = pa.Field(nullable=False)
    arrival_year: Series[int] = pa.Field(nullable=False)
    arrival_date: Series[int] = pa.Field(nullable=False)
    market_segment_type: Series[int] = pa.Field(nullable=False)
    repeated_guest: Series[int] = pa.Field(nullable=False)
    no_of_previous_cancellations: Series[int] = pa.Field(nullable=False)
    no_of_previous_bookings_not_canceled: Series[int] = pa.Field(nullable=False)
    avg_price_per_room: Series[float] = pa.Field(nullable=False)
    no_of_special_requests: Series[int] = pa.Field(nullable=False)
    booking_status: Series[int] = pa.Field(nullable=False)

    @pa.check("no_of_adults")
    def check_lte_4(cls,col):
        return col<=4
    
    @pa.check('type_of_meal_plan')
    def check_lte_3(cls, col):
        return col<=3
    @pa.check('required_car_parking_space')
    def check_lte_1(cls,col):
        return col<=1
    @pa.check('booking_status')
    def check_lte_1_bs(cls,col):
        return col<=1

class SchemaTest(SchemaTrain):
    @classmethod
    def to_schema(cls) -> pa.DataFrameSchema:
        return super().to_schema().remove_columns(["booking_status"])