from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher

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

        # Ici appeler une vraie API ou mocker la réponse
        flights = f"رحلة من {ville_depart} إلى {ville_destination} في {date_depart} بدرجة {classe} ({type_vol})"

        dispatcher.utter_message(text=f"إليك خيارات الرحلات المتاحة: {flights}")
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
