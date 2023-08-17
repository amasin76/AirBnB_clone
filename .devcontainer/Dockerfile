FROM ubuntu:20.04

# Avoid warnings by switching to noninteractive
ENV DEBIAN_FRONTEND=noninteractive

# Install necessary packages
RUN apt-get update && \
    apt-get -y install --no-install-recommends gcc libc6-dev gdb valgrind \
    python3.8 python3-pip git curl zsh man-db locales

# Install additional tools
RUN pip3 install --no-cache-dir pycodestyle==2.8.0 pre-commit && \
    git clone https://github.com/alx-tools/Betty.git /home/Betty && \
    apt-get clean

# Install betty
RUN locale-gen en_US.UTF-8 && \
    update-locale LANG=en_US.UTF-8 && \
    cd /home/Betty && ./install.sh

# Install zsh `robbyrussell` theme
RUN zsh -c "$(curl -fsSL https://raw.githubusercontent.com/robbyrussell/oh-my-zsh/master/tools/install.sh)" ||true

# Clean up
RUN rm -rf /var/lib/apt/lists/* /home/Betty && \
    apt-get remove -y man-db && \
    apt-get autoremove -y && \
    apt-get clean && \
    rm -rf /tmp/* /var/tmp/*

# Set Zsh as the default shell
ENV SHELL="/bin/zsh" PATH="/usr/local/bin:$PATH"

# Switch back to dialog for any ad-hoc use of apt-get
ENV DEBIAN_FRONTEND=dialog
