from cinema_root.db_schema import Reservation
from cinema_root.db import session_scope


class ReservationGateway:
    def add_reservation(self, user_id, projection_id, row, col):
        with session_scope() as session:
            reservation = Reservation(user_id=user_id, projection_id=projection_id, row=row, col=col)
            session.add(reservation)
            raw_reservation = session.query(Reservation)\
                                     .filter(Reservation.user_id == user_id)\
                                     .filter(Reservation.projection_id == projection_id)\
                                     .filter(Reservation.row == row)\
                                     .filter(Reservation.col == col)\
                                     .one()

            raw_dict = raw_reservation.__dict__
            del raw_dict['_sa_instance_state']

            return raw_dict

    def delete_reservation(self, user_id, reservation_id):
        with session_scope() as session:
            session.query(Reservation)\
                   .filter(Reservation.reservation_id == reservation_id)\
                   .filter(Reservation.user_id == user_id)\
                   .delete()

    def find_reservation(self, reservation_id):
        with session_scope() as session:
            raw_reservation = session.query(Reservation).filter(Reservation.reservation_id == reservation_id).one()

            raw_dict = raw_reservation.__dict__
            del raw_dict['_sa_instance_state']

            return raw_dict

    def get_occupied_seats(self, projection_id):
        with session_scope() as session:
            raw_seats_dict = []
            raw_reservations = session.query(Reservation)\
                                      .filter(Reservation.projection_id == projection_id)

            for raw_reservation in raw_reservations:
                raw_dict = raw_reservation.__dict__
                del raw_dict['_sa_instance_state']
                raw_seats_dict.append(raw_dict)

            return raw_seats_dict

    def get_all_reservations(self):
        with session_scope() as session:
            raw_reservations_dict = []
            raw_reservations = session.query(Reservation)

            for raw_reservation in raw_reservations:
                raw_dict = raw_reservation.__dict__
                del raw_dict['_sa_instance_state']
                raw_reservations_dict.append(raw_dict)

            return raw_reservations_dict

    def get_my_reservations(self, user_id):
        with session_scope() as session:
            raw_reservations_dict = []
            raw_reservations = session.query(Reservation)\
                                      .filter(Reservation.user_id == user_id)

            for raw_reservation in raw_reservations:
                raw_dict = raw_reservation.__dict__
                del raw_dict['_sa_instance_state']
                raw_reservations_dict.append(raw_dict)

            return raw_reservations_dict
