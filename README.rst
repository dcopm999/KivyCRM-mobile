=============================
KivyCRM
=============================

Kivy CRM android application


Features
--------

* TODO


Usage
-----

Linux requirements
~~~~~~~~~~~~~~~~~~

add to /etc/apt/sources.list repository record:

    deb http://mirror.yandex.ru/debian/ oldstable main

    
sudo apt-get install python3-distutils python3-dev python3-pip

sudo apt install -y git zip unzip python3-pip autoconf autotools-dev openjdk-8-jdk libtool pkg-config zlib1g-dev libncurses5-dev libncursesw5-dev libtinfo5 cmake libffi-dev libltdl-dev liblld-7-dev llvm-7-dev libssl-dev virtualenvwrapper


sudo pip3 install -r ./requirements.txt

change java version to 1.8 with command:

    sudo update-alternatives --config java

git clone https://github.com/kivy/buildozer.git
cd buildozer
sudo python3 setup.py install

Launching the app
~~~~~~~~~~~~~~~~~

`Kivy`_ is compatible with Python 2 as well as Python 3::

    cd kivycrm
    python main.py

Running the testsuite
~~~~~~~~~~~~~~~~~~~~~

Run its testsuite either with Python3::

    cd kivycrm
    python -m unittest discover

Or with `nose`_::

    cd kivycrm
    nosetests

Or with `py.test`_::

    cd kivycrm
    py.test

Deploying to Android
~~~~~~~~~~~~~~~~~~~~

You can easily run the app on Android by using the `Kivy Launcher`_.


License
-------

Distributed under the terms of the `MIT license`_, kivycrm free and open source software


Issues
------

Report bugs at https://github.com/dcopm999/kivycrm/issues.


.. _`Kivy Launcher`: http://kivy.org/docs/guide/packaging-android.html#packaging-your-application-for-the-kivy-launcher
.. _`Kivy`: https://github.com/kivy/kivy
.. _`MIT License`: http://opensource.org/licenses/MIT
.. _`nose`: https://github.com/nose-devs/nose/
.. _`py.test`: http://pytest.org/latest/
