;; Auto-generated. Do not edit!


(when (boundp 'localizer_dwm1001::Anchor)
  (if (not (find-package "LOCALIZER_DWM1001"))
    (make-package "LOCALIZER_DWM1001"))
  (shadow 'Anchor (find-package "LOCALIZER_DWM1001")))
(unless (find-package "LOCALIZER_DWM1001::ANCHOR")
  (make-package "LOCALIZER_DWM1001::ANCHOR"))

(in-package "ROS")
;;//! \htmlinclude Anchor.msg.html


(defclass localizer_dwm1001::Anchor
  :super ros::object
  :slots (_id _x _y _z _distanceFromTag ))

(defmethod localizer_dwm1001::Anchor
  (:init
   (&key
    ((:id __id) "")
    ((:x __x) 0.0)
    ((:y __y) 0.0)
    ((:z __z) 0.0)
    ((:distanceFromTag __distanceFromTag) 0.0)
    )
   (send-super :init)
   (setq _id (string __id))
   (setq _x (float __x))
   (setq _y (float __y))
   (setq _z (float __z))
   (setq _distanceFromTag (float __distanceFromTag))
   self)
  (:id
   (&optional __id)
   (if __id (setq _id __id)) _id)
  (:x
   (&optional __x)
   (if __x (setq _x __x)) _x)
  (:y
   (&optional __y)
   (if __y (setq _y __y)) _y)
  (:z
   (&optional __z)
   (if __z (setq _z __z)) _z)
  (:distanceFromTag
   (&optional __distanceFromTag)
   (if __distanceFromTag (setq _distanceFromTag __distanceFromTag)) _distanceFromTag)
  (:serialization-length
   ()
   (+
    ;; string _id
    4 (length _id)
    ;; float64 _x
    8
    ;; float64 _y
    8
    ;; float64 _z
    8
    ;; float64 _distanceFromTag
    8
    ))
  (:serialize
   (&optional strm)
   (let ((s (if strm strm
              (make-string-output-stream (send self :serialization-length)))))
     ;; string _id
       (write-long (length _id) s) (princ _id s)
     ;; float64 _x
       (sys::poke _x (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _y
       (sys::poke _y (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _z
       (sys::poke _z (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;; float64 _distanceFromTag
       (sys::poke _distanceFromTag (send s :buffer) (send s :count) :double) (incf (stream-count s) 8)
     ;;
     (if (null strm) (get-output-stream-string s))))
  (:deserialize
   (buf &optional (ptr- 0))
   ;; string _id
     (let (n) (setq n (sys::peek buf ptr- :integer)) (incf ptr- 4) (setq _id (subseq buf ptr- (+ ptr- n))) (incf ptr- n))
   ;; float64 _x
     (setq _x (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _y
     (setq _y (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _z
     (setq _z (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;; float64 _distanceFromTag
     (setq _distanceFromTag (sys::peek buf ptr- :double)) (incf ptr- 8)
   ;;
   self)
  )

(setf (get localizer_dwm1001::Anchor :md5sum-) "f88a18beacac202e25d2f4ff87870a24")
(setf (get localizer_dwm1001::Anchor :datatype-) "localizer_dwm1001/Anchor")
(setf (get localizer_dwm1001::Anchor :definition-)
      "string id
float64  x
float64  y
float64  z
float64  distanceFromTag
")



(provide :localizer_dwm1001/Anchor "f88a18beacac202e25d2f4ff87870a24")


