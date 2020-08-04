;; Auto-generated. Do not edit!


(when (boundp 'localizer_dwm1001::Anchor_3)
  (if (not (find-package "LOCALIZER_DWM1001"))
    (make-package "LOCALIZER_DWM1001"))
  (shadow 'Anchor_3 (find-package "LOCALIZER_DWM1001")))
(unless (find-package "LOCALIZER_DWM1001::ANCHOR_3")
  (make-package "LOCALIZER_DWM1001::ANCHOR_3"))
(unless (find-package "LOCALIZER_DWM1001::ANCHOR_3REQUEST")
  (make-package "LOCALIZER_DWM1001::ANCHOR_3REQUEST"))
(unless (find-package "LOCALIZER_DWM1001::ANCHOR_3RESPONSE")
  (make-package "LOCALIZER_DWM1001::ANCHOR_3RESPONSE"))

(in-package "ROS")





(defclass localizer_dwm1001::Anchor_3Request
  :super ros::object
  :slots ())

(defmethod localizer_dwm1001::Anchor_3Request
  (:init
   (&key
    )
   (send-super :init)
   self)
  (:serialization-length
   ()
   (+
    0
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;;
   self)
  )

(defclass localizer_dwm1001::Anchor_3Response
  :super ros::object
  :slots (_x _y _z ))

(defmethod localizer_dwm1001::Anchor_3Response
  (:init
   (&key
    ((:x __x) 0.0)
    ((:y __y) 0.0)
    ((:z __z) 0.0)
    )
   (send-super :init)
   (setq _x (float __x))
   (setq _y (float __y))
   (setq _z (float __z))
   self)
  (:x
   (&optional __x)
   (if __x (setq _x __x)) _x)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:z
   (&optional __z)
   (if __z (setq _z __z)) _z)
  (:serialization-length
   ()
   (+
    ;; float64 _x
    8
    ;; float64 _y
    8
    ;; float64 _z
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; float64 _x
       (sys::poke _x (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _y
       (sys::poke _y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _z
       (sys::poke _z (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; float64 _x
     (setq _x (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _y
     (setq _y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _z
     (setq _z (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(defclass localizer_dwm1001::Anchor_3
  :super ros::object
  :slots ())

(setf (get localizer_dwm1001::Anchor_3 :md5sum-) "4a842b65f413084dc2b10fb484ea7f17")
(setf (get localizer_dwm1001::Anchor_3 :datatype-) "localizer_dwm1001/Anchor_3")
(setf (get localizer_dwm1001::Anchor_3 :request) localizer_dwm1001::Anchor_3Request)
(setf (get localizer_dwm1001::Anchor_3 :response) localizer_dwm1001::Anchor_3Response)

(defmethod localizer_dwm1001::Anchor_3Request
  (:response () (instance localizer_dwm1001::Anchor_3Response :init)))

(setf (get localizer_dwm1001::Anchor_3Request :md5sum-) "4a842b65f413084dc2b10fb484ea7f17")
(setf (get localizer_dwm1001::Anchor_3Request :datatype-) "localizer_dwm1001/Anchor_3Request")
(setf (get localizer_dwm1001::Anchor_3Request :definition-)
      "---
float64 x
float64 y
float64 z
")

(setf (get localizer_dwm1001::Anchor_3Response :md5sum-) "4a842b65f413084dc2b10fb484ea7f17")
(setf (get localizer_dwm1001::Anchor_3Response :datatype-) "localizer_dwm1001/Anchor_3Response")
(setf (get localizer_dwm1001::Anchor_3Response :definition-)
      "---
float64 x
float64 y
float64 z
")



(provide :localizer_dwm1001/Anchor_3 "4a842b65f413084dc2b10fb484ea7f17")


