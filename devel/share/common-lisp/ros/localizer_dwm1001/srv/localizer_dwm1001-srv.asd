
(cl:in-package :asdf)

(defsystem "localizer_dwm1001-srv"
  :depends-on (:roslisp-msg-protocol :roslisp-utils )
  :components ((:file "_package")
    (:file "Anchor_0" :depends-on ("_package_Anchor_0"))
    (:file "_package_Anchor_0" :depends-on ("_package"))
    (:file "Anchor_1" :depends-on ("_package_Anchor_1"))
    (:file "_package_Anchor_1" :depends-on ("_package"))
    (:file "Anchor_2" :depends-on ("_package_Anchor_2"))
    (:file "_package_Anchor_2" :depends-on ("_package"))
    (:file "Anchor_3" :depends-on ("_package_Anchor_3"))
    (:file "_package_Anchor_3" :depends-on ("_package"))
    (:file "Tag_srv" :depends-on ("_package_Tag_srv"))
    (:file "_package_Tag_srv" :depends-on ("_package"))
  ))