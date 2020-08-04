
(cl:in-package :asdf)

(defsystem "localizer_dwm1001-msg"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Anchor" :depends-on ("_package_Anchor"))
    (:file "_package_Anchor" :depends-on ("_package"))
    (:file "Tag" :depends-on ("_package_Tag"))
    (:file "_package_Tag" :depends-on ("_package"))
  ))