# SlicerDocker platform image
# (based on https://github.com/dit4c/dockerfile-dit4c-container-slicer)

FROM stevepieper/x11
MAINTAINER pieper@isomics.com

RUN apt-get update
RUN apt-get install -y libglu1-mesa
RUN apt-get install -y r-cran-rgl
RUN apt-get install -y firefox-esr
RUN wget https://s3.amazonaws.com/rstudio-dailybuilds/rstudio-xenial-1.0.153-amd64.deb
RUN apt-get install -y ./rstudio-xenial-1.0.153-amd64.deb

# Slicer 4.5: http://download.slicer.org/bitstream/461634
# Slicer 4.6.2 http://download.slicer.org/bitstream/561384"
# Slicer 4.8.0 http://download.slicer.org/bitstream/561384"
# Slicer 4.8.1 http://download.slicer.org/bitstream/738960"

# Slicer Summer 2020 Workshop version
RUN SLICER_URL="https://download.slicer.org/bitstream/1310652" && \
  curl -v -s -L $SLICER_URL | tar xz -C /tmp && \
  mv /tmp/Slicer* /opt/slicer

# copy /opt after extraction slicer (/opt/slicer is extracted tar)
COPY /etc /etc
COPY /opt /opt
COPY /usr /usr


# See http://na-mic.org/Mantis/view.php?id=4015
RUN su researcher -c "mkdir /home/researcher/Documents"
COPY /home/researcher/Documents /home/researcher/Documents
RUN chown -R researcher:researcher /home/researcher/Documents

#copy extension installer script to the container and run the script inside the container. 
#COPY extensions.py /home/researcher/
#RUN /opt/slicer/Slicer --no-main-window --python-script /home/researcher/extensions.py


#COPY /home/researcher/.config /home/researcher/.config
#RUN chown -R researcher:researcher /home/researcher/.config

RUN LNUM=$(sed -n '/launcher_item_app/=' /etc/tint2/panel.tint2rc | head -1) && \
  sed -i "${LNUM}ilauncher_item_app = /opt/slicer/slicer.desktop" /etc/tint2/panel.tint2rc

# Note that slicer is started automatically at login from /etc/skel/.xinitrc
# it will run whatever is in the user's home directory .slicerrc.py, so any
# users of this docker image have the option of putting arbitrary startup commands in that file.
#
# Note also you can set the SLICER_ARGUMENTS environment variable using the -e "SLICER_ARGUMENTS=<value>"
# on the docker run command line.
