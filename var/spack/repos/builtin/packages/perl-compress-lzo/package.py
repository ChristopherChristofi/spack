# Copyright 2013-2023 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
# Copyright 2023 EMBL-European Bioinformatics Institute
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack.package import *


class PerlCompressLzo(PerlPackage):
    """Interface to the LZO compression library"""

    homepage = "https://metacpan.org/pod/Compress::LZO"
    url = "https://cpan.metacpan.org/authors/id/P/PE/PEPL/Compress-LZO-1.09.tar.gz"

    maintainers("EbiArnie")

    version("1.09", sha256="15dbcb5ae4be2da09545b891c66077da5b45e4842f2b99919d29973ff6be4f47")

    depends_on("perl@5.4.0:", type=("build", "link", "run", "test"))
    depends_on("perl-devel-checklib@0.9:", type=("build"))
    depends_on("lzo", type=("build", "link", "run"))

    def test_use(self):
        """Test 'use module'"""
        options = ["-we", 'use strict; use Compress::LZO; print("OK\n")']

        perl = self.spec["perl"].command
        out = perl(*options, output=str.split, error=str.split)
        assert "OK" in out
