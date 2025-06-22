from datetime import datetime, date, time, timedelta

def calculate_duration(start_time: time, end_time: time, date_context: date = date.today()) -> float:
    """
    Calculate the duration in minutes between two times on a given date.
    Handles overnight durations by rolling into the next day.
    
    Args:
        start_time (time): Start time.
        end_time (time): End time.
        date_context (date): The date for context (default is today).
    
    Returns:
        float: Duration in minutes.
    """


    start_dt = datetime.combine(date_context, start_time)
    end_dt = datetime.combine(date_context, end_time)
    if end_dt < start_dt:
        end_dt += timedelta(days=1)  # handle overnight gigs
    duration = end_dt - start_dt
    return duration.total_seconds() / 60  # return duration in minutes

def calculate_total_pay(base_pay: float, tip: float) -> float:
    """
    Calculate the total pay for the gig by adding the tip to the base pay

    Args:
        base_pay (float): Gig app's stated base pay.
        tip (float): Tip received

    Returns:
        float: Total pay.
    ToDo: Compare anticipated total to actual total
    """
    return base_pay + tip

def calculate_mileage(start_mile: float, end_mile: float) -> float:
    """
    Calculates the total mileage per gig trip.

    Args: 
        start_mile (float): The mileage on the odometer when the trip starts
        end_mile (float): The mileage on the odometer when the trip ends

    Returns:
        float: total mileage of the trip.
    """
    return end_mile - start_mile
