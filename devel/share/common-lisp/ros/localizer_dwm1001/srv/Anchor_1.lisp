; Auto-generated. Do not edit!


(cl:in-package localizer_dwm1001-srv)


;//! \htmlinclude Anchor_1-request.msg.html

(cl:defclass <Anchor_1-request> (roslisp-msg-protocol:ros-message)
  ()
)

(cl:defclass Anchor_1-request (<Anchor_1-request>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Anchor_1-request>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Anchor_1-request)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name localizer_dwm1001-srv:<Anchor_1-request> is deprecated: use localizer_dwm1001-srv:Anchor_1-request instead.")))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Anchor_1-request>) ostream)
  "Serializes a message object of type '<Anchor_1-request>"
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Anchor_1-request>) istream)
  "Deserializes a message object of type '<Anchor_1-request>"
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Anchor_1-request>)))
  "Returns string type for a service object of type '<Anchor_1-request>"
  "localizer_dwm1001/Anchor_1Request")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Anchor_1-request)))
  "Returns string type for a service object of type 'Anchor_1-request"
  "localizer_dwm1001/Anchor_1Request")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Anchor_1-request>)))
  "Returns md5sum for a message object of type '<Anchor_1-request>"
  "4a842b65f413084dc2b10fb484ea7f17")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Anchor_1-request)))
  "Returns md5sum for a message object of type 'Anchor_1-request"
  "4a842b65f413084dc2b10fb484ea7f17")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Anchor_1-request>)))
  "Returns full string definition for message of type '<Anchor_1-request>"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Anchor_1-request)))
  "Returns full string definition for message of type 'Anchor_1-request"
  (cl:format cl:nil "~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Anchor_1-request>))
  (cl:+ 0
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Anchor_1-request>))
  "Converts a ROS message object to a list"
  (cl:list 'Anchor_1-request
))
;//! \htmlinclude Anchor_1-response.msg.html

(cl:defclass <Anchor_1-response> (roslisp-msg-protocol:ros-message)
  ((x
    :reader x
    :initarg :x
    :type cl:float
    :initform 0.0)
   (y
    :reader y
    :initarg :y
    :type cl:float
    :initform 0.0)
   (z
    :reader z
    :initarg :z
    :type cl:float
    :initform 0.0))
)

(cl:defclass Anchor_1-response (<Anchor_1-response>)
  ())

(cl:defmethod cl:initialize-instance :after ((m <Anchor_1-response>) cl:&rest args)
  (cl:declare (cl:ignorable args))
  (cl:unless (cl:typep m 'Anchor_1-response)
    (roslisp-msg-protocol:msg-deprecation-warning "using old message class name localizer_dwm1001-srv:<Anchor_1-response> is deprecated: use localizer_dwm1001-srv:Anchor_1-response instead.")))

(cl:ensure-generic-function 'x-val :lambda-list '(m))
(cl:defmethod x-val ((m <Anchor_1-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader localizer_dwm1001-srv:x-val is deprecated.  Use localizer_dwm1001-srv:x instead.")
  (x m))

(cl:ensure-generic-function 'y-val :lambda-list '(m))
(cl:defmethod y-val ((m <Anchor_1-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader localizer_dwm1001-srv:y-val is deprecated.  Use localizer_dwm1001-srv:y instead.")
  (y m))

(cl:ensure-generic-function 'z-val :lambda-list '(m))
(cl:defmethod z-val ((m <Anchor_1-response>))
  (roslisp-msg-protocol:msg-deprecation-warning "Using old-style slot reader localizer_dwm1001-srv:z-val is deprecated.  Use localizer_dwm1001-srv:z instead.")
  (z m))
(cl:defmethod roslisp-msg-protocol:serialize ((msg <Anchor_1-response>) ostream)
  "Serializes a message object of type '<Anchor_1-response>"
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'x))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'y))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
  (cl:let ((bits (roslisp-utils:encode-double-float-bits (cl:slot-value msg 'z))))
    (cl:write-byte (cl:ldb (cl:byte 8 0) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 8) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 16) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 24) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 32) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 40) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 48) bits) ostream)
    (cl:write-byte (cl:ldb (cl:byte 8 56) bits) ostream))
)
(cl:defmethod roslisp-msg-protocol:deserialize ((msg <Anchor_1-response>) istream)
  "Deserializes a message object of type '<Anchor_1-response>"
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'x) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'y) (roslisp-utils:decode-double-float-bits bits)))
    (cl:let ((bits 0))
      (cl:setf (cl:ldb (cl:byte 8 0) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 8) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 16) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 24) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 32) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 40) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 48) bits) (cl:read-byte istream))
      (cl:setf (cl:ldb (cl:byte 8 56) bits) (cl:read-byte istream))
    (cl:setf (cl:slot-value msg 'z) (roslisp-utils:decode-double-float-bits bits)))
  msg
)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql '<Anchor_1-response>)))
  "Returns string type for a service object of type '<Anchor_1-response>"
  "localizer_dwm1001/Anchor_1Response")
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Anchor_1-response)))
  "Returns string type for a service object of type 'Anchor_1-response"
  "localizer_dwm1001/Anchor_1Response")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql '<Anchor_1-response>)))
  "Returns md5sum for a message object of type '<Anchor_1-response>"
  "4a842b65f413084dc2b10fb484ea7f17")
(cl:defmethod roslisp-msg-protocol:md5sum ((type (cl:eql 'Anchor_1-response)))
  "Returns md5sum for a message object of type 'Anchor_1-response"
  "4a842b65f413084dc2b10fb484ea7f17")
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql '<Anchor_1-response>)))
  "Returns full string definition for message of type '<Anchor_1-response>"
  (cl:format cl:nil "float64 x~%float64 y~%float64 z~%~%~%"))
(cl:defmethod roslisp-msg-protocol:message-definition ((type (cl:eql 'Anchor_1-response)))
  "Returns full string definition for message of type 'Anchor_1-response"
  (cl:format cl:nil "float64 x~%float64 y~%float64 z~%~%~%"))
(cl:defmethod roslisp-msg-protocol:serialization-length ((msg <Anchor_1-response>))
  (cl:+ 0
     8
     8
     8
))
(cl:defmethod roslisp-msg-protocol:ros-message-to-list ((msg <Anchor_1-response>))
  "Converts a ROS message object to a list"
  (cl:list 'Anchor_1-response
    (cl:cons ':x (x msg))
    (cl:cons ':y (y msg))
    (cl:cons ':z (z msg))
))
(cl:defmethod roslisp-msg-protocol:service-request-type ((msg (cl:eql 'Anchor_1)))
  'Anchor_1-request)
(cl:defmethod roslisp-msg-protocol:service-response-type ((msg (cl:eql 'Anchor_1)))
  'Anchor_1-response)
(cl:defmethod roslisp-msg-protocol:ros-datatype ((msg (cl:eql 'Anchor_1)))
  "Returns string type for a service object of type '<Anchor_1>"
  "localizer_dwm1001/Anchor_1")