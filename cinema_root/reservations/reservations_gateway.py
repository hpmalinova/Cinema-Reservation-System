from cinema_root.db import Database, Reservation


class ReservationGateway:
    def __init__(self):
        self.db = Database

    def add_reservation(self, user_id, projection_id, row, col):  # DONE?
        session = self.db.create_session()

        try:
            session.query(Reservation).filter(Reservation.projection_id == projection_id)\
                                      .filter(Reservation.row == row)\
                                      .filter(Reservation.col == col)\
                                      .one()
        except Exception:
            session.close()
            return False

        session.add_all([
            Reservation(user_id=user_id, projection_id=projection_id, row=row, col=col)
        ])
        session.commit()

        raw_reservation = session.query(Reservation).filter(Reservation.user_id == user_id)\
                                                    .filter(Reservation.projection_id == projection_id)\
                                                    .filter(Reservation.row == row)\
                                                    .filter(Reservation.col == col)\
                                                    .one()

        raw_dict = raw_reservation.__dict__
        del raw_dict['_sa_instance_state']

        session.close()
        return raw_dict

    def delete_reservation(self, user_id, reservation_id):  # DONE?
        session = self.db.create_session()
        session.query(Reservation).filter(Reservation.id == reservation_id)\
                                  .filter(Reservation.user_id == user_id)\
                                  .delete()
        session.commit()
        session.close()

    def find_reservation(self, id):  # DONE?
        session = self.db.create_session()

        try:
            raw_reservation = session.query(Reservation).filter(Reservation.id == id).one()
        except Exception:
            session.close()
            return False

        raw_dict = raw_reservation.__dict__
        del raw_dict['_sa_instance_state']

        session.close()
        return raw_dict

    def get_occupied_seats(self, projection_id):  # DONE?
        session = self.db.create_session()
        raw_seats_dict = []

        try:
            raw_reservations = session.query(Reservation).filter(Reservation.projection_id == projection_id)
        except Exception:
            session.close()
            return False

        for raw_reservation in raw_reservations:
            raw_dict = raw_reservation.__dict__
            del raw_dict['_sa_instance_state']
            raw_seats_dict.append(raw_dict)

        session.close()
        return raw_seats_dict

    def get_all_reservations(self):  # DONE?
        session = self.db.create_session()
        raw_reservations_dict = []

        try:
            raw_reservations = session.query(Reservation)
        except Exception:
            session.close()
            return False

        for raw_reservation in raw_reservations:
            raw_dict = raw_reservation.__dict__
            del raw_dict['_sa_instance_state']
            raw_reservations_dict.append(raw_dict)

        session.close()
        return raw_reservations_dict

    def get_my_reservations(self, user_id):  # DONE
        session = self.db.create_session()
        raw_reservations_dict = []

        try:
            raw_reservations = session.query(Reservation).filter(Reservation.user_id == user_id)
        except Exception:
            session.close()
            return False

        for raw_reservation in raw_reservations:
            raw_dict = raw_reservation.__dict__
            del raw_dict['_sa_instance_state']
            raw_reservations_dict.append(raw_dict)

        session.close()
        return raw_reservations_dict
