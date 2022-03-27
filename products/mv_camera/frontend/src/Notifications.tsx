import React, {FunctionComponent} from 'react';
import {ReactNotifications, Store} from "react-notifications-component";

import 'react-notifications-component/dist/theme.css'

export function notify(notification: any) {
  Store.addNotification({
    title: notification["title"],
    message: notification["message"],
    type: notification["type"],
    insert: "top",
    container: "top-right",
    animationIn: ["animate__animated", "animate__fadeIn"],
    animationOut: ["animate__animated", "animate__fadeOut"],
    dismiss: {
      duration: 4000
    }
  })
}

export interface NotificationsProps {
}

export const Notifications: FunctionComponent<NotificationsProps> = (props) => {
  return (
    <ReactNotifications/>
  );
};
