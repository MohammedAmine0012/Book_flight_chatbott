from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests

class ActionBookFlight(Action):

    def name(self) -> Text:
        return "action_book_flight"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        ville_depart = tracker.get_slot("ville_depart")
        ville_destination = tracker.get_slot("ville_destination")
        date_depart = tracker.get_slot("date_depart")
        date_retour = tracker.get_slot("date_retour")
        classe = tracker.get_slot("classe")
        type_vol = tracker.get_slot("type_vol")

        # --- Integrate Travelpayouts API call here ---
        token = 'f5f51cb0da31f68c244d98f5e989a9c1'
        # Note: Travelpayouts API requires IATA codes for origin and destination.
        # We would need a way to convert city names (from slots) to IATA codes.
        # For this example, I'll use placeholder IATA codes (NYC and LAX) as in your example.
        # In a real application, you'd need to handle this mapping.
        origin_iata = 'NYC' # Placeholder - replace with logic to get IATA from ville_depart
        destination_iata = 'LAX' # Placeholder - replace with logic to get IATA from ville_destination

        url = f'https://api.travelpayouts.com/v2/prices/latest'

        params = {
            'currency': 'USD',
            'origin': origin_iata,
            'destination': destination_iata,
            'token': token,
            # You might also add 'depart_date' and 'return_date' based on slots
            # 'depart_date': date_depart, # Need to format date correctly
            # 'return_date': date_retour # Need to format date correctly
        }

        try:
            response = requests.get(url, params=params)
            response.raise_for_status() # Raise an exception for bad status codes (4xx or 5xx)
            data = response.json()

            flights_info = []
            # Assuming the API returns a list of flights in 'data' or a similar key
            # You'll need to check the actual API response structure
            if data and 'data' in data:
                 # This part depends heavily on the exact API response structure
                 # For now, let's just print the raw data and indicate success
                 print(f"Travelpayouts API response data: {data['data']}")
                 flights_info.append("Flight search successful (details in logs).") # Placeholder message
            else:
                 flights_info.append("Could not retrieve flight information.")
                 print(f"Travelpayouts API returned no flight data: {data}")

            # Format the response message
            # You would loop through flights_info to show actual flight options
            message = "إليك خيارات الرحلات المتاحة: " + ", ".join(flights_info)

        except requests.exceptions.RequestException as e:
            message = "عذراً، لم أتمكن من البحث عن رحلات الطيران في الوقت الحالي."
            print(f"Error calling Travelpayouts API: {e}")
        except Exception as e:
            message = "حدث خطأ أثناء معالجة طلبك."
            print(f"An unexpected error occurred: {e}")

        dispatcher.utter_message(text=message)
        return []

class ActionBookHotel(Action):

    def name(self) -> Text:
        return "action_book_hotel"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        categorie = tracker.get_slot("categorie_hotel")
        ville = tracker.get_slot("ville_hotel")
        quartier = tracker.get_slot("quartier_hotel")
        nombre_personnes = tracker.get_slot("nombre_personnes")

        hotels = f"فندق {categorie} في {ville}، حي {quartier} لـ {nombre_personnes} أشخاص."

        dispatcher.utter_message(text=f"إليك الفنادق المتاحة: {hotels}")
        return []

class ActionConfirmReservation(Action):

    def name(self) -> Text:
        return "action_confirm_reservation"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="تم تأكيد حجزك، شكراً لثقتك بنا!")
        return []

class ActionChangeOption(Action):

    def name(self) -> Text:
        return "action_change_option"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="حسناً، ما هو الخيار الذي تريد تغييره؟")
        return []
